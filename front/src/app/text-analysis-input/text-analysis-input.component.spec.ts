import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TextAnalysisInputComponent } from './text-analysis-input.component';

describe('TextAnalysisInputComponent', () => {
  let component: TextAnalysisInputComponent;
  let fixture: ComponentFixture<TextAnalysisInputComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TextAnalysisInputComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TextAnalysisInputComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
