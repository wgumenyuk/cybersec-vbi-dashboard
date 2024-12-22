<script lang="ts" generics="T extends Record<string, any>">
	import {
		ArrowDownNarrowWideIcon,
		ArrowDownWideNarrowIcon,
		SearchIcon
	} from "lucide-svelte";

	// Types
	import type { Snippet } from "svelte";

	type SortDirection = "asc" | "desc";

	let {
		columns,
		data,
		row
	}: {
		columns: string[];
		// eslint-disable-next-line no-undef
		data: T[];
		// eslint-disable-next-line no-undef
		row: Snippet<[item: T]>;
	} = $props();

	let searchQuery = $state<string>("");
	let sortColumn = $state<string>("");
	let sortDirection = $state<SortDirection>("asc");

	// eslint-disable-next-line no-undef
	const filter = (data: T[]) => {
		return data
			.filter((row) => {
				if (searchQuery.length === 0) {
					return row;
				}

				return Object.values(row).some((value) =>
					String(value)
						.toLowerCase()
						.includes(searchQuery.toLowerCase())
				);
			})
			.sort((a, b) => {
				if (!sortColumn) {
					return 0;
				}

				const comparison = String(a[sortColumn]).localeCompare(
					String(b[sortColumn])
				);

				return sortDirection === "asc" ? comparison : -comparison;
			});
	};

	const sort = (column: string) => {
		if (sortColumn === column) {
			sortDirection = sortDirection === "asc" ? "desc" : "asc";
			return;
		}

		sortColumn = column;
		sortDirection = "asc";
	};

	let filteredData = $derived(filter(data));
</script>

<div>
	<!-- Search -->
	<div class="flex items-center justify-between pb-4 pr-4">
		<div class="flex items-center bg-slate-100 pl-4">
			<SearchIcon class="text-slate-600" />
			<input
				type=" text"
				placeholder="Search..."
				bind:value={searchQuery}
				class="min-w-96 bg-transparent py-2.5 pl-2.5 text-slate-600 placeholder:text-slate-500"
			/>
		</div>
		<span class="text-sm text-slate-500"
			>Showing {filteredData.length} item{filteredData.length === 1
				? ""
				: "s"}</span
		>
	</div>

	<!-- Header -->
	<div
		class="flex items-center justify-between gap-4 rounded bg-slate-200 p-4"
	>
		{#each columns as column}
			<button
				onclick={() => sort(column)}
				class="flex w-full items-center gap-2 font-bold text-slate-600"
			>
				<span>{column}</span>
				{#if sortColumn === column}
					{#if sortDirection === "asc"}
						<ArrowDownWideNarrowIcon />
					{:else}
						<ArrowDownNarrowWideIcon />
					{/if}
				{/if}
			</button>
		{/each}
	</div>

	<!-- Body -->
	<div class="flex flex-col justify-between">
		{#each filteredData as data}
			<div
				class="flex w-full items-center gap-2 p-4 text-slate-600 even:bg-slate-100"
			>
				{@render row(data)}
			</div>
		{/each}
	</div>
</div>
