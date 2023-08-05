"Main interface for elastic-inference service"
from mypy_boto3_elastic_inference.client import (
    ElasticInferenceClient as Client,
    ElasticInferenceClient,
)


__all__ = ("Client", "ElasticInferenceClient")
