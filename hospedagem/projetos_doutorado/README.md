# Hospedagem dos Projetos do Doutorado

Este projeto disponibiliza uma arquitetura web com:

- Frontend: Next.js
- Backend: FastAPI (Python)
- Orquestracao: Docker Compose

## Estrutura

- `frontend/`: interface web para interagir com os experimentos
- `backend/`: API Python com logica dos automatos

## Subir localmente

```bash
docker compose up --build -d
```

Acessos:

- Frontend: http://localhost:8089
- Backend: http://localhost:3000/docs

## Parar

```bash
docker compose down
```

## Proximo passo

- Adicionar novas rotas no backend para outros trabalhos do doutorado.
- Criar novas paginas no frontend para cada experimento.
