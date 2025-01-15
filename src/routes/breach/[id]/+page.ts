import data from "$lib/data/breaches_symbols.json";

// Types
import type { EntryGenerator } from "./$types";

export const entries: EntryGenerator = () => {
	return data.map((d) => {
		return {
			id: d.ID.toString()
		};
	});
};
