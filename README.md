# HMLAB
Personalized software

A company needed to streamline the entry of users, work done, as well as the generation of invoices. To address this, I developed software that centralizes these processes, making them faster, more organized, and easier to manage.

The program generates a directory to save all the data (wich is not shown on the github repository).

Descripción Técnica del Proyecto
Objetivo General

Desarrollar un Sistema de Gestión para Laboratorio Dental compuesto por una aplicación web responsiva, con versiones adaptadas para ordenadores (Desktop) y dispositivos móviles (Mobile), basado en una arquitectura cliente-servidor, priorizando un backend robusto, seguro y escalable, mientras que el frontend tendrá un diseño minimalista, intuitivo y orientado a la productividad.

Funcionalidades Principales
1. Gestión de Usuarios y Control de Acceso

Implementar un sistema de autenticación con control de acceso basado en roles (RBAC), permitiendo restringir funcionalidades según el nivel de permisos del usuario.

Funcionalidades
Inicio y cierre de sesión.
Administración de usuarios.
Gestión de roles y permisos.
Restablecimiento de contraseñas.
Control de sesiones.
Roles iniciales
Administrador
Técnico Jefe
Técnico
Recepcionista (opcional)
2. Gestión de Pacientes

Permitir la administración completa de la información de los pacientes.

Funcionalidades
Registrar pacientes.
Modificar información.
Buscar pacientes mediante filtros.
Consultar historial de trabajos.
Asociar uno o varios doctores responsables.
3. Gestión de Doctores

Administración de los profesionales que derivan trabajos al laboratorio.

Funcionalidades
Registrar doctores.
Modificar información.
Buscar doctores.
Asociar pacientes.
Consultar historial de trabajos asociados.
4. Catálogo de Trabajos Dentales

Administración del catálogo de servicios ofrecidos por el laboratorio.

Cada tipo de trabajo deberá incluir:

Nombre
Categoría
Descripción
Precio parcial/base
Estado (Activo/Inactivo)
Restricciones

Los valores económicos solo serán visibles para usuarios autorizados.

5. Gestión de Órdenes de Trabajo

Registro y seguimiento de los trabajos realizados para cada paciente.

Cada orden deberá contener:

Paciente
Doctor
Tipo de trabajo
Observaciones
Fecha
Usuario creador
Estado
Estados
Pendiente
Aprobada
Cancelada
Finalizada
6. Flujo de Aprobación

Toda modificación crítica deberá pasar por un proceso de validación.

Los técnicos podrán:

Registrar pacientes.
Registrar trabajos.
Modificar información permitida.

Las acciones críticas quedarán como Solicitud Pendiente, requiriendo aprobación manual por parte del usuario autorizado.

El responsable podrá:

Aprobar
Rechazar
Cancelar

cada solicitud.

7. Auditoría y Trazabilidad

El sistema deberá mantener un registro completo de todas las operaciones realizadas.

Cada modificación almacenará:

Usuario creador
Usuario modificador
Fecha
Hora
Acción realizada
Valor anterior
Valor nuevo

Ninguna modificación importante deberá perder su historial.

8. Sistema de Permisos

Los permisos deberán gestionarse por rol.

Ejemplos:

Técnico
Registrar pacientes
Modificar pacientes
Registrar trabajos
Técnico Jefe

Además de las funciones anteriores:

Visualizar valores monetarios.
Crear nuevos tipos de trabajo.
Modificar tipos de trabajo.
Eliminar registros.
Aprobar órdenes de trabajo.
Administrador

Acceso completo al sistema.

9. Gestión de Cuentas

El sistema permitirá generar cuentas automáticamente utilizando múltiples criterios de búsqueda.

Filtros
Paciente
Doctor
Tipo de trabajo
Estado
Usuario
Fecha
Rango de fechas
Clínica
Otros filtros parametrizables
Exportación
PDF
Excel
10. Base de Datos Centralizada

Toda la información será almacenada en una base de datos en la nube, permitiendo el acceso simultáneo desde múltiples equipos.

Características:

Información centralizada.
Consistencia de datos.
Sincronización en tiempo real.
Respaldo automático.
Recuperación ante fallos.
11. Plataforma Web

El sistema será desarrollado como una aplicación web.

Versión Desktop

Optimizada para:

Pantallas grandes.
Uso intensivo.
Gestión administrativa.
Operaciones complejas.
Versión Mobile

Optimizada para:

Tablets.
Smartphones.
Registro rápido de información.
Consulta de pacientes.
Consulta de órdenes.
Aprobación de solicitudes.

La versión móvil priorizará rapidez y simplicidad, mostrando únicamente las funciones relevantes para el trabajo en terreno.

Requisitos No Funcionales
Arquitectura
Cliente–Servidor.
API REST.
Backend desacoplado del Frontend.
Escalable.
Modular.
Seguridad
Autenticación mediante JWT.
Control de acceso basado en roles (RBAC).
Cifrado de contraseñas.
Registro de auditoría.
Protección frente a accesos no autorizados.
Rendimiento
Tiempo de respuesta inferior a 2 segundos para operaciones comunes.
Soporte para múltiples usuarios concurrentes.
Optimización de consultas a la base de datos.
Disponibilidad
Acceso desde cualquier dispositivo autorizado.
Sincronización automática entre computadores.
Copias de seguridad periódicas.
Usabilidad
Interfaz minimalista.
Navegación intuitiva.
Diseño responsivo.
Adaptación automática a escritorio y dispositivos móviles.
Tecnologías Recomendadas
Componente	Tecnología
Backend	FastAPI (Python)
Base de datos	PostgreSQL
ORM	SQLAlchemy
Migraciones	Alembic
Autenticación	JWT + Passlib
API	REST
Frontend Web	React + Tailwind CSS
Frontend Móvil	React Native (compartiendo lógica con React) o una PWA responsiva si no se requiere una app nativa
Reportes	ReportLab / OpenPyXL
Despliegue	Docker + Nginx
Servidor	Uvicorn + Gunicorn
Infraestructura	VPS o servicios cloud (AWS, Azure o Google Cloud)