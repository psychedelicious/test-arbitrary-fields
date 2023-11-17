from pydantic import BaseModel, Field
from invokeai.app.invocations.baseinvocation import (
    BaseInvocation,
    BaseInvocationOutput,
    Input,
    InputField,
    InvocationContext,
    OutputField,
    invocation,
    invocation_output,
)


class ArbitraryField(BaseModel):
    """A field with some value"""

    value: str = Field(description="The value")


@invocation_output("arbitrary_field_output")
class ArbitraryFieldOutput(BaseInvocationOutput):
    """Base class for nodes that output a single some field"""

    my_field: ArbitraryField = OutputField()


@invocation(
    "arbitrary_field_test_1",
    title="Arbitrary Field Test 1",
    version="1.0.0",
)
class ArbitraryFieldTest1(BaseInvocation):
    """A test primitive"""

    def invoke(self, context: InvocationContext) -> ArbitraryFieldOutput:
        return ArbitraryFieldOutput(my_field=ArbitraryField(value="test"))


@invocation(
    "arbitrary_field_test_2",
    title="Arbitrary Field Test 2",
    version="1.0.0",
)
class ArbitraryFieldTest2(BaseInvocation):
    """A test primitive"""

    my_field: ArbitraryField = InputField(
        description="Some field", input=Input.Connection
    )

    def invoke(self, context: InvocationContext) -> ArbitraryFieldOutput:
        return ArbitraryFieldOutput(my_field=self.my_field)
