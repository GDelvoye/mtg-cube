import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CubeChartComponent } from './cube-chart.component';

describe('CubeChartComponent', () => {
  let component: CubeChartComponent;
  let fixture: ComponentFixture<CubeChartComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CubeChartComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CubeChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
