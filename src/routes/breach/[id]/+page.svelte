<script lang="ts">
	import { page } from "$app/state";

	// Components
	import { ArrowRightIcon } from "lucide-svelte";
	import Card from "$components/Card.svelte";
	import Link from "$components/Link.svelte";
	import StockPriceChangeKPI from "$components/viz/StockPriceChangeKPI.svelte";
	import AffectedPeopleBC from "$components/viz/AffectedPeopleBarChart.svelte";
	import StockPriceChangeComparison from "$components/viz/StockPriceChangeComparison.svelte";

	// Dataset
	import data from "$lib/data/breaches_symbols.json";
	import { onMount } from "svelte";

	const { format: formatDate } = new Intl.DateTimeFormat("en-US", {
		month: "long",
		year: "numeric"
	});

	const { format: formatNumber } = new Intl.NumberFormat("en-US", {
		notation: "compact"
	});

	const { format: formatCurrency } = new Intl.NumberFormat("en-US", {
		style: "currency",
		currency: "USD"
	});

	const parseDate = (date: string) => {
		const [month, year] = date.split("-").map(Number);

		if (!isNaN(month) && !isNaN(year)) {
			return formatDate(new Date(year, month - 1));
		}

		return "";
	};

	const { id } = page.params;
	const breach = data.find((b) => b.ID === Number(id));

	const pre = breach?.Pre !== null ? Number(breach?.Pre) : null;
	const during = breach?.During !== null ? Number(breach?.During) : null;
	const post = breach?.Post !== null ? Number(breach?.Post) : null;

	let stockChange = $state<number>();

	onMount(() => {
		if (
			typeof pre === "number" &&
			typeof during === "number" &&
			typeof post === "number"
		) {
			stockChange = ((post - pre) / pre) * 100;
		}
	});
</script>

<div class="flex w-full flex-col gap-6">
	<Card class="flex w-full justify-between gap-6">
		<div class="flex w-full flex-col gap-6">
			{#if breach}
				<div class="flex items-center gap-4">
					<Link
						href="https://finance.yahoo.com/quote/{breach.Symbol}"
					>
						<span class="text-2xl font-bold">{breach.Company}</span>
					</Link>
					<span
						class="rounded px-2 py-1 text-sm dark:bg-silver-800 dark:text-silver-400"
						>{breach.Symbol}</span
					>
				</div>

				<!-- Industry -->
				<div class="flex flex-col gap-1">
					<span
						class="text-sm font-bold uppercase dark:text-silver-400"
						>Industry</span
					>
					<span>{breach.Industry}</span>
				</div>

				<!-- Breach Type -->
				<div class="flex flex-col gap-1">
					<span
						class="text-sm font-bold uppercase dark:text-silver-400"
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
					<span
						class="text-sm font-bold uppercase dark:text-silver-400"
						>Date</span
					>
					<span>{parseDate(breach.Date)}</span>
				</div>

				<!-- Affected -->
				<div class="flex flex-col gap-1">
					<span
						class="text-sm font-bold uppercase dark:text-silver-400"
						># of Affected</span
					>
					{#if typeof breach.Affected === "number"}
						<span>{formatNumber(breach.Affected)}</span>
					{:else}
						<span>Unknown / Undisclosed</span>
					{/if}
				</div>

				<!-- Stock Change -->
				<div class="flex flex-col gap-1">
					<span
						class="text-sm font-bold uppercase dark:text-silver-400"
						>Stock Change</span
					>
					{#if stockChange && pre && during && post}
						<span
							class={[
								stockChange < 0 &&
									"text-rose-600 dark:text-rose-400",
								stockChange > 0 &&
									"text-emerald-600 dark:text-emerald-400"
							]}
							>{stockChange > 0 ? "+" : ""}{stockChange.toFixed(
								2
							)}%
							<span class="dark:text-silver-400"
								>({formatCurrency(Number(breach.Pre))}
								<ArrowRightIcon size="1em" class="inline" />
								{formatCurrency(Number(breach.Post))})</span
							>
						</span>
					{:else}
						<span>Undeterminable due to incomplete data</span>
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

	<!-- Div 2 (Bar Chart) and Third Component in 50%-50% Split -->
	<div class="flex flex-row gap-6">
		<!-- Bar Chart -->
		<Card class="flex w-full flex-col justify-between gap-8">
			<span class="text-sm font-bold uppercase dark:text-silver-400">
				Affected People in Comparison
			</span>
			<AffectedPeopleBC breachID={Number(id)} />
		</Card>

		<!-- Third Component -->
		<Card class="flex w-full flex-col justify-between gap-8">
			<span class="text-sm font-bold uppercase dark:text-silver-400">
				Stock Price Change Comparison
			</span>
			<StockPriceChangeComparison breachID={Number(id)} />
		</Card>
	</div>
</div>
