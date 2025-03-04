<script lang="ts">
	import {
		ArrowDownIcon,
		ArrowUpIcon,
		SearchIcon,
		XIcon
	} from "lucide-svelte";
	import Title from "$components/Title.svelte";
	import Nav from "$components/Nav.svelte";
	import Breadcrumbs from "$components/Breadcrumbs.svelte";
	import Card from "$components/Card.svelte";
	import Table from "$components/Table.svelte";
	import Link from "$components/Link.svelte";
	import BreachKPI from "$components/viz/BreachKPI.svelte";
	import Heatmap from "$components/viz/Heatmap.svelte";
	import StockByType from "$components/viz/StockPriceImpactByType.svelte";
	import DonutChart from "$components/viz/DonutChart.svelte";

	// Dataset
	import dataset from "$lib/data/breaches_symbols.json";

	const placeholders = [
		"Apple",
		"Microsoft",
		"AAPL",
		"MSFT",
		"Technology",
		"Retail",
		"Source Code Leak",
		"Data Breach"
	];

	const { format: formatNumber } = new Intl.NumberFormat("de-DE");

	let searchQuery = $state<string>("");

	let filteredData = $derived.by(() => {
		if (!searchQuery) {
			return dataset;
		}

		return dataset.filter((item) => {
			return Object.values(item)
				.flat()
				.some((value) =>
					value
						?.toString()
						?.toLowerCase()
						?.includes(searchQuery.toLowerCase())
				);
		});
	});
</script>

{#snippet row(item: (typeof dataset)[0])}
	{@const { ID, Company, Symbol, Industry, Date, Type, Affected } = item}
	{@const StockChange = item["Stock Change"]}
	<span class="block w-full">
		<Link href={`/breach/${ID}`}>{Company}</Link>
	</span>
	<span class="block w-full">
		<Link href={`/breach/${ID}`}>{Symbol}</Link>
	</span>
	<span class="block w-full">{Industry}</span>
	<span class="block w-full">{Date}</span>
	<span class="block w-full">{Type.join(", ")}</span>
	<span class="block w-full">
		{typeof Affected === "number" ? formatNumber(Affected) : Affected}
	</span>
	{#if StockChange}
		<span
			class={[
				"flex",
				"items-center",
				"gap-1.5",
				"w-full",
				StockChange < 0 && "text-rose-600 dark:text-rose-400",
				StockChange > 0 && "text-emerald-600 dark:text-emerald-400"
			]}
		>
			{#if StockChange < 0}
				<ArrowDownIcon size="1em" />
			{:else if StockChange > 0}
				<ArrowUpIcon size="1em" />
			{/if}
			{(StockChange > 0 ? "+" : "") + StockChange.toFixed(2)}%
		</span>
	{:else}
		<span class="block w-full">Unknown</span>
	{/if}
{/snippet}

<Title value="Breach Analysis" />

<Nav title="Breach Analysis" previous="/how">
	<Breadcrumbs
		nodes={[
			{
				label: "Dashboard",
				href: "/"
			},
			{
				label: "Breach Analysis",
				href: "/what"
			}
		]}
	/>
</Nav>

<div class="flex gap-8">
	<div class="mb-8 flex w-[65%] flex-col gap-8">
		<div class="flex h-32 justify-between gap-8">
			<BreachKPI />
		</div>
		<Card class="flex h-16 items-center justify-between">
			<div
				class="relative flex w-fit items-center gap-2 rounded bg-silver-200/75 pl-2 dark:bg-silver-800/50"
			>
				<SearchIcon class="text-silver-400 dark:text-silver-500" />
				<input
					type="text"
					placeholder="Try searching: {placeholders[
						Math.floor(Math.random() * placeholders.length)
					]}"
					class="min-w-72 bg-transparent py-2 pr-9 shadow-sm outline-none placeholder:text-silver-400 dark:shadow-none placeholder:dark:text-silver-500"
					bind:value={searchQuery}
				/>
				{#if searchQuery.length > 0}
					<button
						class="absolute right-0 -translate-x-2"
						onclick={() => (searchQuery = "")}
					>
						<XIcon class="text-silver-500" />
					</button>
				{/if}
			</div>
			<span class="text-silver-500"
				>Showing {filteredData.length} item{filteredData.length === 1
					? ""
					: "s"}</span
			>
		</Card>
		<Card class="h-[calc(100vh-theme(height.8)*13)] overflow-y-auto">
			<Table
				columns={[
					"Company",
					"Symbol",
					"Industry",
					"Date",
					"Type",
					"Affected",
					"Stock Change"
				]}
				rows={filteredData}
				{row}
			/>
		</Card>
		<Card class="text-center">
			<span class="dark:text-silver-400"
				>Breach Distribution amongst Types and Industries</span
			>
			<div class="h-full w-full">
				<Heatmap />
			</div>
		</Card>
	</div>
	<div class="mb-8 flex w-[35%] flex-col gap-8">
		<Card class="align-center flex grow flex-col text-center">
			<span class="pb-8 dark:text-silver-400"
				>Stock Price Impact by Breach Type</span
			>
			<StockByType />
		</Card>
		<Card class="align-center flex grow flex-col text-center">
			<span class="pb-8 dark:text-silver-400"
				>Number of People Affected by Breach Type</span
			>
			<DonutChart />
		</Card>
	</div>
</div>
