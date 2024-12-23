<script lang="ts">
	import Link from "$components/Link.svelte";
	import Table from "$components/Table.svelte";

	// Data
	import data from "$lib/data/breaches_symbols.json";

	const { format } = new Intl.NumberFormat("de-DE");
</script>

{#snippet row(item: (typeof data)[0])}
	<div class="w-full">
		<Link href="/what/{item.Symbol}">{item.Company}</Link>
	</div>
	<div class="w-full">
		<Link href="/what/{item.Symbol}">{item.Symbol}</Link>
	</div>
	<span class="w-full">{item.Industry}</span>
	<span class="w-full">{item.Date}</span>
	<span class="w-full">{item.Type.join(", ")}</span>
	<span class="w-full">
		{!isNaN(item.Affected as number)
			? format(item.Affected as number)
			: item.Affected}
	</span>
{/snippet}

<Table
	columns={["Company", "Symbol", "Industry", "Date", "Type", "Affected"]}
	{data}
	{row}
/>
