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

	const breach = data.find((d) => d.ID === breachID);

	const pre = breach?.Pre !== null ? Number(breach?.Pre) : null;
	const during = breach?.Pre !== null ? Number(breach?.During) : null;
	const post = breach?.Pre !== null ? Number(breach?.Post) : null;

	let theme = $state(document.documentElement.dataset.theme);

	onMount(() => {
		if (!breach || !pre || !during || !post) {
			return;
		}

		const breachDate = parseDate(breach.Date);

		if (!breachDate) {
			return;
		}

		const before = new Date(breachDate);
		before.setMonth(breachDate.getMonth() - 1);

		const after = new Date(breachDate);
		after.setMonth(breachDate.getMonth() + 1);

		const prices = [breach.Pre, breach.During, breach.Post].map(Number);

		new Chart(canvas, {
			type: "line",
			data: {
				labels: [
					`${formatDate(before)} (Before)`,
					`${formatDate(breachDate)} (During)`,
					`${formatDate(after)} (After)`
				],
				datasets: [
					{
						label: "Stock Price (USD)",
						data: prices,
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
							color: (ctx) => {
								if (theme === "light") {
									return ctx.tick.value === 1
										? "rgba(0, 0, 0, 0.5)"
										: "rgba(0, 0, 0, 0.25)";
								}

								return ctx.tick.value === 1
									? "rgba(255, 255, 255, 0.5)"
									: "rgba(255, 255, 255, 0.25)";
							},
							lineWidth: (ctx) => (ctx.tick.value === 1 ? 2 : 1)
						}
					},
					y: {
						display: true,
						title: {
							display: true,
							text: "Stock Price (USD)"
						},
						suggestedMin: 0,
						suggestedMax: Math.round(Math.max(...prices)) + 10,
						grid: {
							color:
								theme === "dark"
									? "rgba(255, 255, 255, 0.25)"
									: "rgba(0, 0, 0, 0.25)"
						}
					}
				}
			}
		});
	});
</script>

<canvas bind:this={canvas}></canvas>

{#if !pre || !during || !post}
	<span class="dark:text-silver-400"
		>Can't show stock diagram due to incomplete data.</span
	>
{/if}
