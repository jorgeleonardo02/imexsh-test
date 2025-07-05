import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { AreaResult } from '../models/area-e.model';

@Injectable({
  providedIn: 'root'
})
export class StainAreaService {

  // Lista local para guardar todos los resultados de los cálculos.
  private results: AreaResult[] = [];

  // BehaviorSubject de RxJS para emitir la lista cada vez que cambia.
  private resultsSubject = new BehaviorSubject<AreaResult[]>([]);

  // Observable público para que los componentes se suscriban con | async.
  results$ = this.resultsSubject.asObservable();

  /**
   * Calcula el área de una mancha usando el método Monte Carlo.
   * @param file La imagen binaria subida por el usuario.
   * @param points Cantidad de puntos aleatorios a generar.
   * @returns Promise<AreaResult> con los datos del cálculo.
   */
  async calculateStainArea(file: File, points: number): Promise<AreaResult> {
    return new Promise<AreaResult>((resolve) => {

      // Crear un objeto Image en memoria.
      const img = new Image();

      // Crear una URL temporal para el archivo de imagen.
      img.src = URL.createObjectURL(file);

      // Ejecutar cuando la imagen ya esté cargada.
      img.onload = () => {

        // Crear un <canvas> en memoria para poder dibujar la imagen.
        const canvas = document.createElement('canvas');

        // Obtener el contexto 2D para dibujar.
        const ctx = canvas.getContext('2d')!;

        // Ajustar el tamaño del canvas al tamaño de la imagen.
        canvas.width = img.width;
        canvas.height = img.height;

        // Dibujar la imagen dentro del canvas.
        ctx.drawImage(img, 0, 0);

        // Obtener todos los datos de píxeles RGBA de la imagen.
        const imgData = ctx.getImageData(0, 0, img.width, img.height);
        const pixels = imgData.data; // Array plano con R,G,B,A,R,G,B,A...

        // Inicializar contador de puntos dentro de la mancha.
        let insidePoints = 0;

        // Repetir para cada punto aleatorio.
        for (let i = 0; i < points; i++) {
          // Generar coordenadas X e Y aleatorias dentro de la imagen.
          const x = Math.floor(Math.random() * img.width);
          const y = Math.floor(Math.random() * img.height);

          // Calcular el índice base del píxel en el array (4 bytes por píxel).
          const index = (y * img.width + x) * 4;

          // Obtener valores RGB de ese píxel.
          const r = pixels[index];
          const g = pixels[index + 1];
          const b = pixels[index + 2];

          // Verificar si es blanco (aprox.) → dentro de la mancha.
          if (r > 200 && g > 200 && b > 200) {
            insidePoints++;
          }
        }

        // Calcular área total de la imagen.
        const totalArea = img.width * img.height;

        // Calcular área estimada proporcional.
        const estimatedArea = totalArea * (insidePoints / points);

        // Crear objeto de resultado con todos los datos.
        const result: AreaResult = {
          id: Date.now(),             // Usar timestamp como ID.
          totalPoints: points,        // Total de puntos generados.
          insidePoints,               // Cuántos quedaron dentro de la mancha.
          estimatedArea,              // Área estimada final.
          date: new Date()            // Fecha y hora del cálculo.
        };

        // Guardar el resultado en la lista.
        this.results.push(result);

        // Notificar a todos los observadores del nuevo resultado.
        this.resultsSubject.next(this.results);

        // Resolver la promesa devolviendo el resultado.
        resolve(result);
      };
    });
  }
}