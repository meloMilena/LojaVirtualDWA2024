from fastapi import APIRouter

from dtos.excluir_produto_dto import ExcluirProdutoDTO
from dtos.inserir_produto_dto import InserirProdutoDTO
from models.produto_model import Produto
from repositories.produto_repo import ProdutoRepo


router = APIRouter(prefix="/manager")


@router.get("/obter_produtos")
async def obter_produtos():
    produtos = ProdutoRepo.obter_todos()
    return produtos

@router.post("/inserir_produto")
async def inserir_produto(produto: InserirProdutoDTO) -> Produto:
    novo_produto = Produto(None, produto.nome, produto.preco, produto.descricao, produto.estoque)
    novo_produto = ProdutoRepo.inserir(novo_produto)
    return novo_produto


# @router.get("/excluir_produto")
# async def excluir_produto(produto: ExcluirProdutoDTO) -> Produto:
#     produto = ProdutoRepo.obter_um(produto.id)
#     produto = ProdutoRepo.excluir(produto)
#     return produto
