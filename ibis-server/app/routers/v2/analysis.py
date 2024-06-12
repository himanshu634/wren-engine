from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.logger import log_dto
from app.mdl.analyzer import analyze

router = APIRouter(prefix="/analysis", tags=["analysis"])


class AnalyzeSQLDTO(BaseModel):
    manifest_str: str = Field(alias="manifestStr", description="Base64 manifest")
    sql: str


@router.get("/sql")
@log_dto
def analyze_sql(dto: AnalyzeSQLDTO) -> list[dict]:
    return analyze(dto.manifest_str, dto.sql)
