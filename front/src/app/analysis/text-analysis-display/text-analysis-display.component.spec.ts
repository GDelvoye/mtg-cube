import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TextAnalysisDisplayComponent } from './text-analysis-display.component';

describe('TextAnalysisDisplayComponent', () => {
  let component: TextAnalysisDisplayComponent;
  let fixture: ComponentFixture<TextAnalysisDisplayComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TextAnalysisDisplayComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TextAnalysisDisplayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
