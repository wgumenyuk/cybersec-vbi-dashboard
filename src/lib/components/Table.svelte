<script lang="ts" generics="T extends Record<string, any>">
	import {
		ArrowDownNarrowWideIcon,
		ArrowDownWideNarrowIcon
	} from "lucide-svelte";

	// Types
	import type { Snippet } from "svelte";

	type SortDirection = "asc" | "desc";

	let {
		columns,
		rows,
		row
	}: {
		columns: string[];
		// eslint-disable-next-line no-undef
		rows: T[];
		// eslint-disable-next-line no-undef
		row: Snippet<[item: T]>;
	} = $props();

	const parseDate = (value: unknown) => {
		const [month, year] = String(value)
			.split("-")
			.map((v) =>
				v.startsWith("0") ? parseInt(v.slice(1)) : parseInt(v)
			);

		if (!isNaN(month) && !isNaN(year)) {
			return new Date(Number(year), Number(month) - 1);
		}

		return null;
	};

	// eslint-disable-next-line @typescript-eslint/no-explicit-any
	const compare = (a: any, b: any, sortDirection: SortDirection) => {
		if (a === b) return 0;
		if (a === "Unknown" && b !== "Unknown") return 1;
		if (a !== "Unknown" && b === "Unknown") return -1;

		const da = parseDate(a);
		const db = parseDate(b);

		if (da && db) {
			return sortDirection === "asc"
				? da.getTime() - db.getTime()
				: db.getTime() - da.getTime();
		}

		if (da && !db) return 1;
		if (!da && db) return -1;

		if (!isNaN(a) && !isNaN(b)) {
			return sortDirection === "asc" ? a - b : b - a;
		}

		if (!isNaN(a) && isNaN(b)) return 1;
		if (isNaN(a) && !isNaN(b)) return -1;

		const comparison = String(a).localeCompare(String(b), undefined, {
			sensitivity: "base"
		});

		return sortDirection === "asc" ? comparison : -comparison;
	};

	const toggleSort = (column: string) => {
		if (sortColumn === column) {
			sortDirection = sortDirection === "asc" ? "desc" : "asc";
			return;
		}

		sortColumn = column;
		sortDirection = "asc";
	};

	let sortColumn = $state<string>("");
	let sortDirection = $state<SortDirection>("asc");

	let sortedRows = $derived(
		!sortColumn
			? rows
			: rows.toSorted((a, b) =>
					compare(a[sortColumn], b[sortColumn], sortDirection)
				)
	);
</script>

<div>
	<div
		class="sticky top-0 mb-2 flex items-center justify-between gap-2 rounded bg-silver-50 p-2 shadow-sm dark:bg-silver-950 dark:shadow-none"
	>
		{#each columns as column}
			<button
				class="flex w-full items-center gap-1"
				onclick={() => toggleSort(column)}
			>
				<span class="font-bold text-silver-700 dark:text-silver-200"
					>{column}</span
				>
				{#if sortColumn === column}
					{#if sortDirection === "asc"}
						<ArrowDownNarrowWideIcon
							size="20px"
							class="dark:text-silver-200"
						/>
					{:else}
						<ArrowDownWideNarrowIcon
							size="20px"
							class="dark:text-silver-200"
						/>
					{/if}
				{/if}
			</button>
		{/each}
	</div>
	<div class="flex flex-col gap-3">
		{#if rows.length > 0}
			{#each sortedRows as item}
				<div
					class="flex justify-between gap-2 rounded p-2 even:bg-silver-300/25 dark:text-silver-400 even:dark:bg-silver-800/25"
				>
					{@render row(item)}
				</div>
			{/each}
		{:else}
			<span class="mx-auto pt-4 dark:text-silver-500"
				>No items found matching your query.</span
			>
		{/if}
	</div>
</div>
