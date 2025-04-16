import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MultiSelectSetComponent } from './multi-select-set.component';

describe('MultiSelectSetComponent', () => {
  let component: MultiSelectSetComponent;
  let fixture: ComponentFixture<MultiSelectSetComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MultiSelectSetComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MultiSelectSetComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
