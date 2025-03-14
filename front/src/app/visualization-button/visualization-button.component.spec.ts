import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VisualizationButtonComponent } from './visualization-button.component';

describe('VisualizationButtonComponent', () => {
  let component: VisualizationButtonComponent;
  let fixture: ComponentFixture<VisualizationButtonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VisualizationButtonComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VisualizationButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
