import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoadCubeSummaryButtonComponent } from './load-cube-summary-button.component';

describe('LoadCubeSummaryButtonComponent', () => {
  let component: LoadCubeSummaryButtonComponent;
  let fixture: ComponentFixture<LoadCubeSummaryButtonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [LoadCubeSummaryButtonComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(LoadCubeSummaryButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
