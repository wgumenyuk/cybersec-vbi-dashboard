<script lang="ts">
	import { onMount } from "svelte";
	import { Chart } from "chart.js/auto";

	// Datset
	import data from "$lib/data/breaches_symbols.json";

	let {
		breachID
	}: {
		breachID: number;
	} = $props();

	let canvas: HTMLCanvasElement;

	const { format: formatDate } = new Intl.DateTimeFormat("en-US", {
		month: "long",
		year: "numeric"
	});

	const { format: formatPrice } = new Intl.NumberFormat("en-US", {
		style: "currency",
		currency: "USD"
	});

	const parseDate = (date: string) => {
		const [month, year] = date.split("-").map(Number);

		if (!isNaN(month) && !isNaN(year)) {
			return new Date(year, month - 1);
		}

		return null;
	};

	onMount(() => {
		const breach = data.find((d) => d.ID === breachID);

		if (!breach) {
			return;
		}

		const during = parseDate(breach.Date);

		if (!during) {
			return;
		}

		const before = new Date(during);
		before.setMonth(during.getMonth() - 1);

		const after = new Date(during);
		after.setMonth(during.getMonth() + 1);

		new Chart(canvas, {
			type: "line",
			data: {
				labels: [
					formatDate(before),
					formatDate(during),
					formatDate(after)
				],
				datasets: [
					{
						label: "Stock Price (USD)",
						data: [breach.Pre, breach.During, breach.Post],
						tension: 0.4
					}
				]
			},
			options: {
				plugins: {
					tooltip: {
						callbacks: {
							label: (ctx) => formatPrice(ctx.parsed.y)
						}
					}
				},
				scales: {
					x: {
						grid: {
							color: "rgba(255, 255, 255, 0.25)"
						}
					},
					y: {
						display: true,
						title: {
							display: true,
							text: "Stock Price (USD)"
						},
						suggestedMin: 0,
						suggestedMax: Math.round(Number(breach.Post)) + 10,
						grid: {
							color: "rgba(255, 255, 255, 0.25)"
						}
					}
				}
			}
		});
	});
</script>

<canvas bind:this={canvas}></canvas>
