import logging
from typing import Type, Any, Dict, Callable, Optional

from graphql import GraphQLSchema, GraphQLObjectType, graphql, OperationType, validate_schema, GraphQLType, \
    GraphQLResolveInfo
from graphql.pyutils import camel_to_snake

from .builder import SchemaBuilder
from .execution import TGQLExecutionContext
from .utils import is_graph, is_connection

logger = logging.getLogger(__name__)
AnyType = Optional[Type[Any]]


class Schema(GraphQLSchema):
    def __init__(self,
                 query: AnyType = None,
                 mutation: AnyType = None,
                 subscription: AnyType = None,
                 types: Dict[str, GraphQLType] = None,
                 camelcase=True):
        super().__init__()
        self.camelcase = camelcase
        builder = SchemaBuilder(self.camelcase, types=types)
        if query:
            self.query = query
            query_fields = builder.get_fields(query)
            query = GraphQLObjectType(
                'Query',
                fields=query_fields,
            )

        if mutation:
            self.mutation: Type = mutation
            mutation_fields = builder.get_fields(mutation)
            mutation = GraphQLObjectType(
                'Mutation',
                fields=mutation_fields
            )

        if subscription:
            self.subscription: object = subscription
            subscription_fields = builder.get_fields(subscription)
            subscription = GraphQLObjectType(
                'Subscription',
                fields=subscription_fields
            )

        super().__init__(query, mutation, subscription)
        errors = validate_schema(self)
        if errors:
            raise errors[0]

    def _field_resolver(self, source, info, **kwargs):
        field_name = info.field_name
        if self.camelcase:
            field_name = camel_to_snake(field_name)

        if info.operation.operation == OperationType.MUTATION and is_graph(source.__class__):
            try:
                mutation = getattr(source, f'mutate_{field_name}')
                return mutation(info, **kwargs)
            except AttributeError:
                return

        if is_graph(source.__class__):
            _type = source.__annotations__.get(field_name)

            if is_connection(_type):
                method = getattr(_type, 'resolve', None)
                if method:
                    return method(source, field_name, _type.__args__[0], info, **kwargs)

        value = (
            source.get(field_name)
            if isinstance(source, dict)
            else getattr(source, f'resolve_{field_name}', getattr(source, field_name, None))
        )
        if callable(value):
            return value(info, **kwargs)
        return value

    async def run(self, query: str,
                  root: Any = None,
                  resolver: Callable[[Any, GraphQLResolveInfo, Dict[str, Any]], Any] = None,
                  operation: str = None, context: Any = None, variables=None,
                  middleware=None, execution_context_class=TGQLExecutionContext):
        if query.startswith('mutation') and not root:
            root = self.mutation()
        elif not root:
            root = self.query()
        result = await graphql(self,
                               query,
                               root_value=root,
                               field_resolver=resolver or self._field_resolver,
                               operation_name=operation,
                               context_value=context,
                               variable_values=variables,
                               middleware=middleware,
                               execution_context_class=execution_context_class)
        return result
