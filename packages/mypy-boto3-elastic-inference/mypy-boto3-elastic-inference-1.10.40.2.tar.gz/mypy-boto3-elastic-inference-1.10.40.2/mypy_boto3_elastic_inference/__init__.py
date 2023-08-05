"Main interface for elastic-inference service"
from mypy_boto3_elastic_inference.client import (
    ElasticInferenceClient,
    ElasticInferenceClient as Client,
)


__all__ = ("Client", "ElasticInferenceClient")
