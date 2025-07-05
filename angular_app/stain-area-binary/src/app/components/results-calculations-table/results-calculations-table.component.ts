import { Component } from '@angular/core';
import { AreaResult } from '../../models/area-e.model';
import { CommonModule } from '@angular/common';
import { StainAreaService } from '../../services/stain-area.service';

@Component({
  selector: 'app-results-calculations-table',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './results-calculations-table.component.html',
  styleUrl: './results-calculations-table.component.scss'
})
/* export class ResultsCalculationsTableComponent {
  results: AreaResult[] = [
    {
      id: 1,
      totalPoints: 1000,
      insidePoints: 300,
      estimatedArea: 30,
      date: new Date()
    }
    // Aquí irían resultados reales desde el servicio
  ];
} */
export class ResultsCalculationsTableComponent {
  results$: typeof this.stainAreaService.results$;

  constructor(private stainAreaService: StainAreaService) {
    this.results$ = this.stainAreaService.results$;
  }
}