<script lang="ts" generics="T extends Record<string, string>">
	import { FilterIcon } from "lucide-svelte";

	let {
		header,
		items
	}: {
		header: string[];
		/* eslint-disable-next-line no-undef */
		items: T[];
	} = $props();

	let filter = $state("");

	const setFilter = (event: Event) => {
		filter = (event.target as HTMLInputElement).value;
	};

	/* eslint-disable-next-line no-undef */
	const applyFilter = (items: T[]) => {
		return items.filter((item) => {
			const cells = Object.values(item)
				.map((item) => item.toLowerCase())
				.join(" ");

			return cells.includes(filter.toLowerCase());
		});
	};

	let itemsView = $derived(!filter ? items : applyFilter(items));
</script>

<div>
	<!-- Input -->
	<div class="flex items-center gap-2 bg-slate-50">
		<FilterIcon class="text-slate-600" />
		<input
			type="text"
			placeholder="Filter..."
			value={filter}
			oninput={setFilter}
			class="min-w-64 bg-transparent px-4 py-2 outline-none placeholder:text-slate-400"
		/>
		<span class="text-xs text-slate-600"
			>Zeige {itemsView.length} von {items.length} Ergebnissen an.</span
		>
	</div>

	<!-- Header -->
	<div class="flex justify-between py-2 font-bold">
		{#each header as cell}
			<span class="block w-full">{cell}</span>
		{/each}
	</div>

	<!-- Body -->
	<div>
		{#each itemsView as item}
			<div
				class="flex justify-between py-2 odd:bg-slate-50 even:bg-slate-100"
			>
				{#each Object.values(item) as cell}
					<span class="block w-full">{cell}</span>
				{/each}
			</div>
		{/each}
	</div>
</div>
