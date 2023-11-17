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


class CustomField(BaseModel):
    """A field with some value"""

    value: str = Field(description="The value")


@invocation_output("custom_field_output")
class CustomFieldOutput(BaseInvocationOutput):
    """Base class for nodes that output a single some field"""

    my_field: CustomField = OutputField()


@invocation(
    "custom_field_test_1",
    title="Custom Field Test 1",
    version="1.0.0",
)
class CustomFieldTest1(BaseInvocation):
    """A test primitive"""

    def invoke(self, context: InvocationContext) -> CustomFieldOutput:
        return CustomFieldOutput(my_field=CustomField(value="test"))


@invocation(
    "custom_field_test_2",
    title="Custom Field Test 2",
    version="1.0.0",
)
class CustomFieldTest2(BaseInvocation):
    """A test primitive"""

    my_field: CustomField = InputField(description="Some field", input=Input.Connection)

    def invoke(self, context: InvocationContext) -> CustomFieldOutput:
        return CustomFieldOutput(my_field=self.my_field)
