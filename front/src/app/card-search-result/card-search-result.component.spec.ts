import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CardSearchResultComponent } from './card-search-result.component';

describe('CardSearchResultComponent', () => {
  let component: CardSearchResultComponent;
  let fixture: ComponentFixture<CardSearchResultComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CardSearchResultComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CardSearchResultComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
