<script lang="ts">
	import { mean, median } from "mathjs";

	// Components
	import Card from "$components/Card.svelte";

	// Dataset
	import data from "$lib/data/breaches_symbols.json";

	const { format } = new Intl.NumberFormat("en-US", {
		notation: "compact"
	});

	const affected = data
		.map((d) => d.Affected)
		.filter((d) => typeof d === "number");

	/**
		Anzahl der aufgezeichneten Breaches im Datensatz.
	*/
	const numberOfBreaches = data.length;

	/**
		Summe aller Betroffenen.
	*/
	const totalAffected = affected.reduce((acc, cur) => acc + cur);

	/**
		Median der Betroffenen.
	*/
	const medianAffected = median(affected);

	/**
		Durchschnittliche Preisänderung (1 Monat vor Angriff - 1 Monat nach Angriff).
	*/

	// Helper function to calculate percentage change
	const calculatePercentageChange = (before: number, after: number): number => {
		return ((after - before) / before) * 100;
	};

	// Calculate the average percentage change in stock price due to breaches

	const averageStockPriceChange = (() => {
		const percentageChanges = data
	        .map((d) => {
	    	// Parse stock prices
                const stockPriceBefore = parseFloat(d["Pre-Attack Stock Price"]);
                const stockPriceAfter = parseFloat(d["Post-Attack Stock Price"]);

                // Check if both values are valid numbers
                if (!isNaN(stockPriceBefore) && !isNaN(stockPriceAfter) && stockPriceBefore !== 0) {
                    return calculatePercentageChange(stockPriceBefore, stockPriceAfter);
                }
                return null; // Skip invalid entries
	    })
    	.filter((change) => change !== null) as number[];

		return percentageChanges.length
			? percentageChanges.reduce((acc, cur) => acc + cur, 0) / percentageChanges.length
			: 0;
	})();

	/**
		Meist-auftretender Breach Type.
	*/
	const mostCommonBreachType = (() => {
		const count = data.reduce((count: Record<string, number>, d) => {
			d.Type.forEach((type: string) => {
				count[type] = (count[type] || 0) + 1;
			});
			return count;
		}, {});

		const type = Object.entries(count).sort((a, b) => {
			const countA = a[1];
			const countB = b[1];
			return countB - countA;
		})[0];

		return type[0];
	})();
</script>

<Card class="flex w-full grow flex-col justify-center gap-4">
	<span class="dark:text-silver-400"># Breaches</span>
	<span class="text-2xl">{numberOfBreaches}</span>
</Card>

<Card class="flex w-full grow flex-col justify-center gap-4">
	<span class="dark:text-silver-400"># Total Affected</span>
	<span class="text-2xl">{format(totalAffected)}</span>
</Card>

<Card class="flex w-full grow flex-col justify-center gap-4">
	<span class="dark:text-silver-400"># Affected per Breach</span>
	<span class="text-2xl">{format(medianAffected)}</span>
</Card>

<Card class="flex w-full grow flex-col justify-center gap-4">
	<span class="dark:text-silver-400">Avg. Stock Price Change</span>
	<span class="text-2xl">{format(averageStockPriceChange)}%</span>
</Card>

<Card class="flex w-full grow flex-col justify-center gap-4">
	<span class="dark:text-silver-400">Most Common Breach Type</span>
	<span class="text-2xl">{mostCommonBreachType}</span>
</Card>
