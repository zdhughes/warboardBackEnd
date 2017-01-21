from troposphere import Output, Parameter, Ref, Template
from troposphere.dynamodb import (KeySchema, AttributeDefinition,
                                  ProvisionedThroughput)
from troposphere.dynamodb import Table


class DynamoTable(object):
    """Clean up resources past their expiration date."""
    def __init__(self):
        """Initialize the necessary Troposphere template."""
        self.template = Template()
        self.add_hash_keys()
        self.add_throughput()
        self.add_tables()


    def add_hash_keys(self): 
        t = self.template
        self.project_hash_key_name = t.add_parameter(Parameter(
            "ProjectKeyName",
            Description="Key Name",
            Type="String",
            Default="ProjectName",
            AllowedPattern="[a-zA-Z0-9]*",
            MinLength="1",
            MaxLength="2048",
            ConstraintDescription="must contain only alphanumberic characters"
        ))

        self.project_hash_key_type = t.add_parameter(Parameter(
            "ProjectKeyType",
            Description="Key Type",
            Type="String",
            Default="S",
            AllowedPattern="[S|N]",
            MinLength="1",
            MaxLength="1",
            ConstraintDescription="must be either S or N"
        ))

        self.person_hash_key_name = t.add_parameter(Parameter(
            "PersonKeyName",
            Description="Key Name",
            Type="String",
            Default="UserName",
            AllowedPattern="[a-zA-Z0-9]*",
            MinLength="1",
            MaxLength="2048",
            ConstraintDescription="must contain only alphanumberic characters"
        ))

        self.person_hash_key_type = t.add_parameter(Parameter(
            "PersonKeyType",
            Description="Key Type",
            Type="String",
            Default="S",
            AllowedPattern="[S|N]",
            MinLength="1",
            MaxLength="1",
            ConstraintDescription="must be either S or N"
        ))

        print "HASH KEY ADDED!"


    def add_throughput(self): 
        t = self.template
        self.read_units = t.add_parameter(Parameter(
            "ReadCapacityUnits",
            Description="Provisioned read throughput",
            Type="Number",
            Default="5",
            MinValue="5",
            MaxValue="10000",
            ConstraintDescription="should be between 5 and 10000"
        ))

        self.write_units = t.add_parameter(Parameter(
            "WriteCapacityUnits",
            Description="Provisioned write throughput",
            Type="Number",
            Default="10",
            MinValue="5",
            MaxValue="10000",
            ConstraintDescription="should be between 5 and 10000"
        ))

        print "THROUGHPUT ADDED!"


    def add_tables(self): 

        print "BEGINNING TO ADD TABLE"
        t = self.template
        self.project_dynamo_table = t.add_resource(Table(
            "projectTable",
            AttributeDefinitions=[
                AttributeDefinition(
                    AttributeName=Ref(self.project_hash_key_name),
                    AttributeType=Ref(self.project_hash_key_type)
                ),
            ],
            KeySchema=[
                KeySchema(
                    AttributeName=Ref(self.project_hash_key_name),
                    KeyType="HASH"
                )
            ],
            ProvisionedThroughput=ProvisionedThroughput(
                ReadCapacityUnits=Ref(self.read_units),
                WriteCapacityUnits=Ref(self.write_units)
            )
        ))

        self.person_dynamo_table = t.add_resource(Table(
            "personTable",
            AttributeDefinitions=[
                AttributeDefinition(
                    AttributeName=Ref(self.person_hash_key_name),
                    AttributeType=Ref(self.person_hash_key_type)
                ),
            ],
            KeySchema=[
                KeySchema(
                    AttributeName=Ref(self.person_hash_key_name),
                    KeyType="HASH"
                )
            ],
            ProvisionedThroughput=ProvisionedThroughput(
                ReadCapacityUnits=Ref(self.read_units),
                WriteCapacityUnits=Ref(self.write_units)
            )
        ))

        print "TABLE ADDED" 


def sceptre_get_template():
    """Retrieve the Sceptre template."""
    lambda_function = DynamoTable()
    return lambda_function.template