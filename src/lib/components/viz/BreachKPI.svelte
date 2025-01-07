<script lang="ts">
	import { median } from "mathjs";

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

	// Helper function to calculate percentage change
	const calculatePercentageChange = (
		before: number,
		after: number
	): number => {
		return ((after - before) / before) * 100;
	};

	// Find the biggest drop in percentage and the associated company
	const biggestDrop = (() => {
		let maxDrop = 0;
		let company = "";

		data.forEach((d) => {
			const stockPriceBefore = parseFloat(d["Pre"]);
			const stockPriceAfter = parseFloat(d["Post"]);

			if (
				!isNaN(stockPriceBefore) &&
				!isNaN(stockPriceAfter) &&
				stockPriceBefore !== 0
			) {
				const percentageChange = calculatePercentageChange(
					stockPriceBefore,
					stockPriceAfter
				);

				// Check if this is the largest drop
				if (percentageChange < maxDrop) {
					maxDrop = percentageChange;
					company = d.Company;
				}
			}
		});

		return {
			company,
			maxDrop
		};
	})();

	/**
		Median der Betroffenen.
	*/
	const medianAffected = median(affected);

	/**
		Durchschnittliche Preisänderung (1 Monat vor Angriff - 1 Monat nach Angriff).
	*/

	// Calculate the average percentage change in stock price due to breaches

	const averageStockPriceChange = (() => {
		const percentageChanges = data
			.map((d) => {
				// Parse stock prices
				const stockPriceBefore = parseFloat(d["Pre"]);
				const stockPriceAfter = parseFloat(d["Post"]);

				// Check if both values are valid numbers
				if (
					!isNaN(stockPriceBefore) &&
					!isNaN(stockPriceAfter) &&
					stockPriceBefore !== 0
				) {
					return calculatePercentageChange(
						stockPriceBefore,
						stockPriceAfter
					);
				}
				return null; // Skip invalid entries
			})
			.filter((change) => change !== null) as number[];

		return percentageChanges.length
			? percentageChanges.reduce((acc, cur) => acc + cur, 0) /
					percentageChanges.length
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

<Card class="flex w-full grow flex-col justify-around gap-4">
	<span class="h-full dark:text-silver-400"># of Breaches</span>
	<span class="text-2xl">{numberOfBreaches}</span>
</Card>

<Card class="flex w-full grow flex-col justify-around gap-4">
	{@const { company, maxDrop } = biggestDrop}
	<span class="h-full dark:text-silver-400">Largest Stock Decline</span>
	<div class="flex items-center gap-4">
		<span class="text-2xl text-rose-600 dark:text-rose-400">
			{format(maxDrop)}%
		</span>
		<span class="text-xs">{company}</span>
	</div>
</Card>

<Card class="flex w-full grow flex-col justify-around gap-4">
	<span class="h-full dark:text-silver-400"># of Affected per Breach</span>
	<span class="text-2xl">{format(medianAffected)}</span>
</Card>

<Card class="flex w-full grow flex-col justify-around gap-4">
	<span class="h-full dark:text-silver-400">Avg. Stock Price Change</span>
	<span class="text-2xl text-emerald-600 dark:text-emerald-400">
		+{format(averageStockPriceChange)}%
	</span>
</Card>

<Card class="flex w-full grow flex-col justify-around gap-4">
	<span class="h-full dark:text-silver-400">Most Common Breach Type</span>
	<span class="text-2xl">{mostCommonBreachType}</span>
</Card>
