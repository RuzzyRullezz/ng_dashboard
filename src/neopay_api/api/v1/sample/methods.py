from fastapi import APIRouter

from .serializers import SampleRequest, SampleResponse


router = APIRouter()


@router.post(
    "/",
    response_model=SampleResponse,
    tags=["Sample"],
    operation_id="sample-method"
)
def sample_method(sample_request: SampleRequest) -> SampleResponse:
    return SampleResponse(msg=str(sample_request.value))


@router.get(
    "/error/",
    response_model=SampleResponse,
    tags=["Sample"],
    operation_id="sample-method-internal-server-error"
)
def sample_method_internal_server_error() -> SampleResponse:
    raise RuntimeError("test error")
