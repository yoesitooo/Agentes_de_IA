# Skill: HTML moderno y semántico

## Objetivo
Generar HTML5 semántico, limpio y bien estructurado.

## Instrucciones obligatorias
- Siempre incluye `<!DOCTYPE html>` y `<html lang="es">`.
- Usa etiquetas semánticas: `<header>`, `<main>`, `<section>`, `<article>`, `<footer>`, `<nav>`, `<aside>`.
- Incluye siempre estas meta tags en el `<head>`:
  ```
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="descripción de la página">
  <title>Título descriptivo</title>
  ```
- Usa atributos `alt` en todas las imágenes.
- Usa atributos `aria-label` en elementos interactivos sin texto visible.
- Estructura jerárquica de encabezados: un solo `<h1>`, luego `<h2>`, `<h3>`, etc.
- Incluye un `<link rel="icon">` con un emoji como favicon usando data URI cuando no haya imagen disponible.

## Buenas prácticas
- Separa estructura (HTML), presentación (CSS) y comportamiento (JS).
- Evita divitis: usa etiquetas semánticas antes de `<div>`.
- Añade `loading="lazy"` a imágenes que no estén en el viewport inicial.
