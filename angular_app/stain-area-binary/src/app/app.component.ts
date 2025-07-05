import { Component } from '@angular/core';
import { MatTabsModule } from '@angular/material/tabs';
//import { RouterOutlet } from '@angular/router';
import { ImageInputCalculatorComponent } from './components/image-input-calculator/image-input-calculator.component';
import { CarouselComponent } from './components/carousel/carousel.component';
import { ResultsCalculationsTableComponent } from './components/results-calculations-table/results-calculations-table.component';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [//RouterOutlet, 
    MatTabsModule,
    ImageInputCalculatorComponent,
    CarouselComponent,
    ResultsCalculationsTableComponent,
    FormsModule
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'stain-area-binary';
}
