from fastapi import APIRouter

router = APIRouter(prefix='/api/v1')


@router.get('/example')
async def get_example():
    return {'example': 'Project is ready!'}