<script lang="ts" generics="T extends Record<string, any>">
	import {
		ArrowDownNarrowWideIcon,
		ArrowDownWideNarrowIcon
	} from "lucide-svelte";

	import type { Snippet } from "svelte";

	type SortDirection = "asc" | "desc";

	let {
		columns,
		rows,
		row
	}: {
		columns: string[];
		/* eslint-disable no-undef */
		rows: T[];
		row: Snippet<[item: T]>;
		/* eslint-enable no-undef */
	} = $props();

	// Declare reactive state variables
	let sortColumn = $state<string>("");
	let sortDirection = $state<SortDirection>("asc");

	const compare = (
		a: unknown,
		b: unknown,
		sortDirection: SortDirection
	): number => {
		if (a === b) return 0;
		if (a === "Unknown") return 1;
		if (b === "Unknown") return -1;

		const dateA = parseDate(a);
		const dateB = parseDate(b);

		if (dateA && dateB) {
			return sortDirection === "asc"
				? dateA.getTime() - dateB.getTime()
				: dateB.getTime() - dateA.getTime();
		}

		if (typeof a === "number" && typeof b === "number") {
			return sortDirection === "asc" ? a - b : b - a;
		}

		return sortDirection === "asc"
			? String(a).localeCompare(String(b))
			: String(b).localeCompare(String(a));
	};

	const parseDate = (value: unknown): Date | null => {
		if (typeof value === "string") {
			const [month, year] = value.split("-").map(Number);
			if (!isNaN(month) && !isNaN(year)) {
				return new Date(year, month - 1);
			}
		}
		return null;
	};

	const toggleSort = (column: string) => {
		if (sortColumn === column) {
			sortDirection = sortDirection === "asc" ? "desc" : "asc";
		} else {
			sortColumn = column;
			sortDirection = "asc";
		}
	};

	let sortedRows = $derived.by(() => {
		if (!sortColumn) return rows;
		return rows
			.slice()
			.sort((a, b) =>
				compare(a[sortColumn], b[sortColumn], sortDirection)
			);
	});
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
			<span class="mx-auto pt-8 dark:text-silver-500"
				>No items found matching your query.</span
			>
		{/if}
	</div>
</div>
