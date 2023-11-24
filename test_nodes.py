from typing import Optional, Union
from pydantic import BaseModel, Field
from invokeai.app.invocations.baseinvocation import (
    BaseInvocation,
    BaseInvocationOutput,
    InputField,
    InvocationContext,
    OutputField,
    invocation,
    invocation_output,
)


class MyField(BaseModel):
    """A field with some value"""

    value: str = Field(description="The value")


class AnotherField(BaseModel):
    """A field with some value"""

    value: str = Field(description="The value")


@invocation_output("custom_field_output")
class MyFieldOutput(BaseInvocationOutput):
    """Base class for nodes that output a single some field"""

    my_field: MyField = OutputField()


@invocation_output("custom_field_2_output")
class AnotherFieldOutput(BaseInvocationOutput):
    """Base class for nodes that output a single some field"""

    my_field: AnotherField = OutputField()


@invocation(
    "custom_field_test_1",
    title="Custom Field Test 1",
    version="1.0.0",
)
class CustomFieldTest1Invocation(BaseInvocation):
    """A test primitive"""

    def invoke(self, context: InvocationContext) -> MyFieldOutput:
        return MyFieldOutput(my_field=MyField(value="test"))


@invocation(
    "custom_field_test_2",
    title="Custom Field Test 2",
    version="1.0.0",
)
class CustomFieldTest2Invocation(BaseInvocation):
    """A test primitive"""

    my_field: Optional[MyField] = InputField(
        default=None, description="Single CustomField"
    )
    my_collection_field: Optional[list[MyField]] = InputField(
        default=None, description="Collection CustomField"
    )
    my_polymorphic_field: Optional[Union[MyField, list[MyField]]] = InputField(
        default=None, description="Polymorphic CustomField"
    )
    another_field: Optional[AnotherField] = InputField(
        default=None, description="Single CustomField2"
    )

    def invoke(self, context: InvocationContext) -> MyFieldOutput:
        return MyFieldOutput(my_field=self.my_field)
