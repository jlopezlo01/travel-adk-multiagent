# Análisis del laboratorio

## ¿Por qué dividir el problema en varios agentes en vez de usar uno solo?

La especialización permite dar instrucciones más concretas, aislar responsabilidades y evaluar cada parte por separado. El coordinador puede combinar investigación, planificación, presupuesto, riesgos y cultura sin cargar todas esas tareas en una sola instrucción. La división también facilita mantener o ampliar una capacidad sin reescribir el resto.

## ¿Qué ventajas tiene que el agente de búsqueda web esté separado?

La búsqueda es la única función que necesita consultar información que cambia con el tiempo. Mantenerla separada ayuda a distinguir datos actuales de recomendaciones generadas, limitar cuándo se usa Internet y pedir que se prioricen fuentes oficiales. El itinerario y el presupuesto pueden trabajar con lo investigado sin duplicar búsquedas.

## ¿Qué riesgos existen cuando un agente consulta información desde Internet?

Puede encontrar datos falsos, desactualizados, incompletos o contradictorios; también resultados sesgados, publicidad o contenido malicioso que intente influir en el agente. Deben revisarse la fuente y la fecha, contrastar afirmaciones importantes y evitar tratar instrucciones halladas en páginas como órdenes del sistema.

## ¿Qué pasaría si la búsqueda entrega información desactualizada o contradictoria?

El coordinador podría transmitir una recomendación equivocada, como horarios, restricciones o precios que ya cambiaron. La respuesta debe identificar incertidumbres, mostrar fuentes y fechas cuando estén disponibles, contrastar fuentes oficiales y recomendar verificar antes de comprar. Si no puede resolver la contradicción, debe decirlo y no presentar una opción como confirmada.

## ¿Cómo podría validarse la calidad de una respuesta multiagente?

Se combinan pruebas unitarias de las herramientas, pruebas de integración de delegación, casos de evaluación con destinos y restricciones conocidas, revisión humana de respuestas y mediciones de factualidad, cobertura de requisitos, utilidad y seguridad. Las respuestas sobre datos cambiantes deben contrastarse con fuentes actuales. Una prueba de estructura no demuestra por sí sola que el modelo siempre responda correctamente.

## ¿Qué diferencia hay entre una arquitectura multiagente y microservicios?

Los agentes son componentes de razonamiento que coordinan modelos y herramientas para completar tareas; pueden compartir el mismo proceso y contexto de conversación. Los microservicios son servicios desplegables por separado, con límites de datos y comunicación de red definidos. Una solución puede usar ambas ideas: agentes especializados implementados como microservicios, aunque no son equivalentes.

## ¿Cómo convertir este laboratorio en una solución empresarial para una agencia?

Conectar inventario y reservas mediante APIs autorizadas, incorporar precios con fecha y moneda, proteger datos personales, autenticar usuarios, registrar auditoría y medir calidad. También hacen falta límites de gasto, manejo de errores, monitoreo, pruebas de seguridad, políticas de privacidad y revisión humana para excepciones, pagos y cambios de reserva. Las recomendaciones deben tener fuentes y dejar claro qué está confirmado.

## ¿Qué información no debería automatizarse sin validación humana?

La elegibilidad migratoria y sanitaria, alertas de seguridad, restricciones oficiales, disponibilidad y precio final de vuelos u hoteles, seguros, pagos, cancelaciones y cualquier decisión que afecte derechos, salud o seguridad. El sistema puede orientar y enlazar fuentes, pero debe advertir que se verifique con la autoridad o proveedor responsable.

## ¿Por qué son importantes las pruebas unitarias si parte del sistema usa IA?

Las herramientas deterministas —por ejemplo, el cálculo de presupuesto— sí pueden verificarse con resultados esperados y límites. Las pruebas también detectan errores de integración y cambios accidentales en los agentes. No prueban que un modelo generativo sea siempre correcto, por eso se complementan con evaluaciones y revisión humana.

## ¿Qué parte representa CI/CD y cuál representa inteligencia artificial?

La integración continua está en GitHub Actions, que instala dependencias y ejecuta Ruff, Pytest y Sonar cuando hay cambios. El sistema de inteligencia artificial está en los agentes de Google ADK y Gemini, que interpretan la solicitud y delegan tareas; Google Search aporta información web. El flujo descrito automatiza validaciones, pero no despliega la aplicación, así que no cubre entrega continua completa.
