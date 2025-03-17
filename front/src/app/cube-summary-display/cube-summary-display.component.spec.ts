import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CubeSummaryDisplayComponent } from './cube-summary-display.component';

describe('CubeSummaryDisplayComponent', () => {
  let component: CubeSummaryDisplayComponent;
  let fixture: ComponentFixture<CubeSummaryDisplayComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CubeSummaryDisplayComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CubeSummaryDisplayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
