# Estado de la entrega

## Preparado en esta carpeta

- Proyecto modular de Google ADK con agente coordinador y cinco subagentes, incluido el reto `LocalCultureAgent`.
- Herramientas de presupuesto y evaluación básica de riesgos.
- Pruebas unitarias para las herramientas y estructura multiagente.
- Ruff, configuración de cobertura, GitHub Actions y Sonar.
- Archivo `.env.example` sin credenciales.
- Respuestas a las preguntas de análisis en `ANALISIS.md`.

## Pasos que requieren tus cuentas o tu participación

1. En `.env`, añade tu `GOOGLE_API_KEY` de Google AI Studio.
2. Ejecuta `poetry install`, `poetry run pytest` y `poetry run ruff check .` en tu equipo.
3. Ejecuta `poetry run adk run travel_assistant` y `poetry run adk web --port 8000`; captura las salidas y prueba un viaje nacional y uno internacional.
4. Crea un repositorio vacío en GitHub, configura el remoto y publica `feature/travel-multiagent`; luego abre un Pull Request hacia `develop`.
5. Configura `SONAR_TOKEN` y `SONAR_HOST_URL` como secretos del repositorio. Cambia `sonar.projectKey` por la clave real de tu proyecto antes de ejecutar el análisis.
6. Guarda capturas reales del Pull Request, GitHub Actions y SonarCloud/SonarQube junto al proyecto. No se incluyen capturas ficticias.

## Comandos Git sugeridos

```powershell
git remote add origin https://github.com/TU_USUARIO/travel-adk-multiagent.git
git push -u origin main
git push -u origin develop
git push -u origin feature/travel-multiagent
```

La identidad Git del equipo se usó para crear el commit local inicial. El proyecto ya tiene las ramas `main`, `develop` y `feature/travel-multiagent`, y el trabajo está en esta última. Aún no hay remoto configurado; crea el repositorio en GitHub y reemplaza `TU_USUARIO` antes de publicar.
