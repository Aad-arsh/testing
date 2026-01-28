from django_elasticsearch_dsl import Document, Index, fields
from .models import employee
from django_elasticsearch_dsl.registries import registry

employee_index = Index("employees")

employee_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@employee_index.document
class EmployeeDocument(Document):

    company = fields.ObjectField(properties={
        "id": fields.KeywordField(),
        "name": fields.TextField()
    })

    Department = fields.ObjectField(properties={
        "id": fields.KeywordField(),
        "name": fields.TextField()
    })

    class Django:
        model = employee
        fields = [
            "id",
            "name",
            "phone",
            "email",
            "designation"
        ]
