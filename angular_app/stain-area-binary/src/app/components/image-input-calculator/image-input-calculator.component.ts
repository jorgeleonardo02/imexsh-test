import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { StainAreaService } from '../../services/stain-area.service';

@Component({
  selector: 'app-image-input-calculator',
  standalone: true, 
  imports: [
    FormsModule 
  ],
  templateUrl: './image-input-calculator.component.html',
  styleUrl: './image-input-calculator.component.scss'
})

export class ImageInputCalculatorComponent {
  uploadedImage: File | null = null;
  points = 1000;

  constructor(private stainAreaService: StainAreaService) {}

  onFileSelected(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.uploadedImage = input.files[0];
    }
  }

  async onCalculate() {
    if (!this.uploadedImage) {
      alert('Por favor, sube una imagen.');
      return;
    }

    const result = await this.stainAreaService.calculateStainArea(this.uploadedImage, this.points);
    console.log('Resultado:', result);
    alert(`Área estimada: ${result.estimatedArea.toFixed(2)} px²`);
  }
}