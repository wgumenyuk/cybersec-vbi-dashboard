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

	const parseDate = (date: string) => {
		if (typeof date !== "string") {
			return null;
		}

		const [month, year] = date.split("-").map((value) => {
			return value.startsWith("0")
				? parseInt(value.slice(1))
				: parseInt(value);
		});

		if (!isNaN(month) && !isNaN(year)) {
			return new Date(Number(year), Number(month) - 1);
		}

		return null;
	};

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

				const x = a[sortColumn];
				const y = b[sortColumn];

				if (x === "Unknown" && y !== "Unknown") return 1;
				if (y === "Unknown" && x !== "Unknown") return -1;
				if (x === "Unknown" && y === "Unknown") return 0;

				const dx = parseDate(x);
				const dy = parseDate(y);

				// X und Y sind Daten.
				if (dx && dy) {
					return sortDirection === "asc"
						? dx.getFullYear() - dy.getFullYear()
						: dy.getFullYear() - dx.getFullYear();
				}

				if (dx && !dy) return -1;
				if (dy && !dy) return 1;

				// X und Y sind Nummern.
				if (!isNaN(x) && !isNaN(y)) {
					return sortDirection === "asc" ? x - y : y - x;
				}

				if (!isNaN(x) && isNaN(y)) return -1;
				if (!isNaN(y) && isNaN(x)) return 1;

				// X und Y sind Strings.
				const comparison = String(x).localeCompare(
					String(y),
					undefined,
					{
						sensitivity: "base"
					}
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
	<div
		class="sticky top-0 flex items-center justify-between rounded-md bg-slate-100 p-4 shadow-sm"
	>
		<div class="flex items-center rounded bg-slate-50 pl-4">
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
		class="sticky top-20 flex items-center justify-between gap-4 rounded-md bg-slate-200 p-4 shadow-sm"
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
	<div class="flex flex-col justify-between overflow-y-auto">
		{#if filteredData.length > 0}
			{#each filteredData as data}
				<div
					class="flex w-full items-center gap-2 p-4 text-slate-600 even:bg-slate-100"
				>
					{@render row(data)}
				</div>
			{/each}
		{:else}
			<span class="mx-auto pt-8 text-slate-400"
				>No items matched "{searchQuery}"</span
			>
		{/if}
	</div>
</div>
