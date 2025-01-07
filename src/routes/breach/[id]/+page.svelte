<script lang="ts">
	import { page } from "$app/stores";

	// Components
	import Card from "$components/Card.svelte";
	import Link from "$components/Link.svelte";
	import StockPriceChangeKPI from "$components/viz/StockPriceChangeKPI.svelte";

	// Dataset
	import data from "$lib/data/breaches_symbols.json";

	const { format: formatDate } = new Intl.DateTimeFormat("en-US", {
		month: "long",
		year: "numeric"
	});

	const { format: formatNumber } = new Intl.NumberFormat("en-US", {
		notation: "compact"
	});

	const parseDate = (date: string) => {
		const [month, year] = date.split("-").map(Number);

		if (!isNaN(month) && !isNaN(year)) {
			return formatDate(new Date(year, month - 1));
		}

		return "";
	};

	const { id } = $page.params;
	const breach = data.find((b) => b.ID === Number(id));
</script>

<Card class="flex w-full gap-12">
	<div class="flex w-full flex-col gap-6">
		{#if breach}
			<div class="flex items-center gap-4">
				<Link href="https://finance.yahoo.com/quote/{breach.Symbol}">
					<span class="text-2xl font-bold">{breach.Company}</span>
				</Link>
				<span
					class="rounded px-2 py-1 text-sm dark:bg-silver-800 dark:text-silver-400"
					>{breach.Symbol}</span
				>
			</div>

			<!-- Industry -->
			<div class="flex flex-col gap-1">
				<span class="text-sm font-bold uppercase dark:text-silver-400"
					>Industry</span
				>
				<span>{breach.Industry}</span>
			</div>

			<!-- Breach Type -->
			<div class="flex flex-col gap-1">
				<span class="text-sm font-bold uppercase dark:text-silver-400"
					>Breach Type</span
				>
				<div class="flex gap-2">
					{#each breach.Type as type}
						<span
							class="rounded px-2 py-1 dark:bg-silver-800 dark:text-silver-400"
							>{type}</span
						>
					{/each}
				</div>
			</div>

			<!-- Date -->
			<div class="flex flex-col gap-1">
				<span class="text-sm font-bold uppercase dark:text-silver-400"
					>Date</span
				>
				<span>{parseDate(breach.Date)}</span>
			</div>

			<!-- Affected -->
			<div class="flex flex-col gap-1">
				<span class="text-sm font-bold uppercase dark:text-silver-400"
					># of Affected</span
				>
				{#if typeof breach.Affected === "number"}
					<span>{formatNumber(breach.Affected)}</span>
				{:else}
					<span>Unknown / Undisclosed</span>
				{/if}
			</div>
		{:else}
			<span>Breach not found.</span>
		{/if}
	</div>
	<div class="w-full">
		<StockPriceChangeKPI breachID={Number(id)} />
	</div>
</Card>
