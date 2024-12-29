<script lang="ts">
	import { onMount } from "svelte";
	import { Chart } from "chart.js/auto";

	// Types
	import type dataset from "$lib/data/breaches_symbols.json";

	let props: { data: typeof dataset } = $props();

	let data = $derived.by(() => {
		const types = props.data.flatMap((d) => d.Type);

		const count = types.reduce((count: Record<string, number>, type) => {
			count[type] = (count[type] || 0) + 1;
			return count;
		}, {});

		return Object.entries(count)
			.map(([label, value]) => ({
				label,
				value
			}))
			.toSorted((a, b) => a.value - b.value);
	});

	let canvas: HTMLCanvasElement;
	let chart: Chart;

	onMount(() => {
		chart = new Chart(canvas, {
			type: "doughnut",
			data: {
				labels: data.map((d) => d.label),
				datasets: [
					{
						data: data.map((d) => d.value)
					}
				]
			},
			options: {
				plugins: {
					legend: {
						display: false
					}
				}
			}
		});
	});

	$effect(() => {
		if (data.length === 0) {
			return;
		}

		if (chart.data.labels?.length === data.length) {
			return;
		}

		chart.data.labels = data.map((d) => d.label);
		chart.data.datasets[0].data = data.map((d) => d.value);

		chart.update();
	});
</script>

{#if data.length === 0}
	<span class="absolute dark:text-silver-500">No data to show.</span>
{/if}

<canvas bind:this={canvas} class={[data.length === 0 && "invisible"]}></canvas>
