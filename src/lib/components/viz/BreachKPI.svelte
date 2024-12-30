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
		Durchschnittliches Intervall zwischen Breaches.
	*/
	const averageBreachInterval = (() => {
		const dates = data
			.map((d) => {
				const date = d.Date.startsWith("0") ? d.Date.slice(1) : d.Date;

				const [month, year] = date.split("-").map((v) => parseInt(v));

				if (month && year) {
					return new Date(year, month - 1);
				}

				return null;
			})
			.filter((date) => date !== null)
			.sort((a, b) => a.getTime() - b.getTime());

		const differences: number[] = [];

		for (let i = 1; i < dates.length; i++) {
			const a = dates[i];
			const b = dates[i - 1];

			differences.push(
				(a.getFullYear() - b.getFullYear()) * 12 +
					a.getMonth() -
					b.getMonth()
			);
		}

		return mean(differences);
	})();

	/**
		Branche mit den meisten Breaches.
	*/
	const mostCommonIndustry = (() => {
		const count = data.reduce((count: Record<string, number>, d) => {
			count[d.Industry] = (count[d.Industry] || 0) + 1;
			return count;
		}, {});

		const industry = Object.entries(count).sort((a, b) => {
			const countA = a[1];
			const countB = b[1];
			return countB - countA;
		})[0];

		return industry[0];
	})();
</script>

<Card class="flex w-full grow flex-col justify-center gap-4">
	<span class="dark:text-silver-400"># Breaches</span>
	<span class="text-4xl">{numberOfBreaches}</span>
</Card>

<Card class="flex w-full grow flex-col justify-center gap-4">
	<span class="dark:text-silver-400"># Total Affected</span>
	<span class="text-4xl">{format(totalAffected)}</span>
</Card>

<Card class="flex w-full grow flex-col justify-center gap-4">
	<span class="dark:text-silver-400"># Affected per Breach</span>
	<span class="text-4xl">{format(medianAffected)}</span>
</Card>

<Card class="flex w-full grow flex-col justify-center gap-4">
	<span class="dark:text-silver-400">Avg. # Months Between Breaches</span>
	<span class="text-4xl">{format(averageBreachInterval)}</span>
</Card>

<Card class="flex w-full grow flex-col justify-center gap-4">
	<span class="dark:text-silver-400">Industry With Most # Breaches</span>
	<span class="text-4xl">{mostCommonIndustry}</span>
</Card>
