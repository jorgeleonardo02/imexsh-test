# Stain Area Binary App

Esta es una aplicación **Angular** que calcula el **área de una mancha** en una **imagen binaria** usando el método **Monte Carlo**.

## Descripción

- **Funcionalidad principal**:
  - Sube una imagen **binaria** (blanco = mancha, negro = fondo).
  - Genera `n` puntos aleatorios dentro de la imagen.
  - Calcula cuántos puntos caen dentro de la mancha blanca.
  - Estima el área de la mancha en proporción al área total de la imagen.
  - Guarda un historial de resultados en una tabla.


## Requisitos previos

- **Node.js** instalado (versión recomendada: >= 18)
- **Angular CLI** instalado globalmente:

  ```bash
  npm install -g @angular/cli

## En IMEXHS_TEST\angular_app\stain-area-binary 
npm install

## Hago 
ng serve -o

## Probar la app de angular