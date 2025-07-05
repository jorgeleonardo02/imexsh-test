export interface AreaResult {
  id: number;               
  totalPoints: number;      // Total de puntos generados (n)
  insidePoints: number;     // Puntos dentro de la mancha (ni)
  estimatedArea: number;    // Área estimada calculada
  date: Date;               // Fecha y hora del cálculo
}