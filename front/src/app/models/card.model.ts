export interface Card {
  id: number;
  name: string;
  oracle_text: string;
  colors: string[]; // ou Color[] si tu veux les typer strictement
  mana_cost?: string;
  type_line?: string;
  id_full: string;
  // Ajoute d'autres champs selon ton backend
}
