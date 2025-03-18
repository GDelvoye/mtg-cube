import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CubeSummarySelectorComponent } from './cube-summary-selector.component';

describe('CubeSummarySelectorComponent', () => {
  let component: CubeSummarySelectorComponent;
  let fixture: ComponentFixture<CubeSummarySelectorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CubeSummarySelectorComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CubeSummarySelectorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
