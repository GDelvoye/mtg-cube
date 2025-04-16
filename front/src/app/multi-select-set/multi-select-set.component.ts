import { CommonModule } from '@angular/common';
import {
  Component,
  EventEmitter,
  Input,
  Output,
  signal,
  ViewChild,
} from '@angular/core';
import { FormControl, ReactiveFormsModule } from '@angular/forms';
import { map, Observable, of, startWith } from 'rxjs';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatChipInputEvent, MatChipsModule } from '@angular/material/chips';
import {
  MatAutocomplete,
  MatAutocompleteModule,
  MatAutocompleteSelectedEvent,
} from '@angular/material/autocomplete';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-multi-select-set',
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MatInputModule,
    MatFormFieldModule,
    MatChipsModule,
    MatAutocompleteModule,
    MatIconModule,
  ],
  templateUrl: './multi-select-set.component.html',
  styleUrl: './multi-select-set.component.scss',
})
export class MultiSelectSetComponent {
  // @ViewChild(MatAutocomplete) auto: MatAutocomplete;
  @Input() label = 'Select options';
  @Input() options: string[] = [];
  @Input() selected: string[] = [];
  @Output() selectedChange = new EventEmitter<string[]>();

  inputControl = new FormControl<string>('');
  filteredOptions$: Observable<string[]> = of([]);

  @ViewChild(MatAutocomplete) auto: MatAutocomplete | undefined;

  ngOnInit() {
    this.filteredOptions$ = this.inputControl.valueChanges.pipe(
      startWith(''),
      map((value) => this._filter(value || ''))
    );
  }

  private _filter(value: string): string[] {
    const filterValue = value.toLowerCase();
    return this.options
      .filter((option) => option.toLowerCase().includes(filterValue))
      .filter((option) => !this.selected.includes(option));
  }

  selectedEvent(event: any): void {
    this.selected = [...this.selected, event.option.viewValue];
    this.selectedChange.emit(this.selected);
    this.inputControl.setValue('');
  }

  add(event: MatChipInputEvent): void {
    const value = (event.value || '').trim();
    if (value && !this.selected.includes(value)) {
      this.selected = [...this.selected, value];
      this.selectedChange.emit(this.selected);
    }
    this.inputControl.setValue('');
  }

  addTextValue(): void {
    const value = this.inputControl.value?.trim();
    if (value && !this.selected.includes(value)) {
      this.selected = [...this.selected, value];
      this.selectedChange.emit(this.selected);
    }
    this.inputControl.setValue('');
  }

  remove(option: string): void {
    const newList = this.selected.filter((item) => item !== option);
    this.selectedChange.emit(newList);
  }
}
