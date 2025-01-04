<script lang="ts">
    import * as d3 from "d3";

    // Dataset
    import data from "$lib/data/breaches_symbols.json";

    // Process data
    const processedData = (() => {
        const impacts: Record<string, number[]> = {};

        data.forEach((d) => {
            const affected = parseFloat(String(d["Affected"]));
            const types = d.Type;

            if (!isNaN(affected) && affected > 0) {
                if (Array.isArray(types)) {
                    types.forEach((type) => {
                        if (type) {
                            if (!impacts[type]) impacts[type] = [];
                            impacts[type].push(affected);
                        }
                    });
                }
            }
        });

        return Object.entries(impacts)
            .map(([type, values]) => ({
                type,
                average: values.reduce((acc, cur) => acc + cur, 0) / values.length,
            }))
            .sort((a, b) => b.average - a.average); // Sort by average descending
    })();

    const width = 600;
    const height = 400;
    const radius = Math.min(width, height) / 2 - 40; // Radius of the chart
    const color = d3.scaleOrdinal([
        "#6c3baa", // Purple
        "#2563eb", // Blue
        "#22c55e", // Green
        "#ef4444", // Red
        "#f59e0b", // Amber
        "#ffde21", // Yellow
        "#6366f1", // Indigo
        "#9333ea", // Violet
        "#e11d48", // Pink
        "#ffb5c0"  // Light Pink
    ]);

    // Pie generator
    const pie = d3.pie<{ type: string; average: number }>()
        .value((d) => d.average)
        .sort(null);

    const arc = d3.arc<d3.PieArcDatum<{ type: string; average: number }>>()
        .innerRadius(radius / 2) // Donut hole size
        .outerRadius(radius);

    let tooltip = { visible: false, x: 0, y: 0, text: "", color: "" };

    function showTooltip(event: MouseEvent, average: number, sliceColor: string) {
        tooltip = {
            visible: true,
            x: event.pageX,
            y: event.pageY - 40,
            text: `${average.toLocaleString()} affected`,
            color: sliceColor,
        };
    }

    function hideTooltip() {
        tooltip.visible = false;
    }
</script>

<div class="flex flex-col items-center">
    <!-- Donut Chart -->
    <svg
        class="w-full h-full"
        viewBox={`0 0 ${width} ${height}`}
    >
        <g transform={`translate(${width / 2}, ${height / 2})`}>
            {#each pie(processedData) as pieData}
                <path
                    d={arc(pieData) || ""}
                    fill={color(pieData.data.type)}
                    class="cursor-pointer opacity-80 hover:opacity-100 transition-opacity"
                    on:mouseenter={(e) => showTooltip(e, pieData.data.average, color(pieData.data.type))}
                    on:mouseleave={hideTooltip}
                    role="graphics-symbol"
                    aria-label={`Slice for ${pieData.data.average.toLocaleString()} people`}
                />
            {/each}
        </g>
    </svg>

    <!-- Legend -->
    <div class="legend grid grid-cols-2 gap-4 mt-6">
        {#each processedData as { type, average }}
            <div class="flex items-center">
                <div
                    class="w-4 h-4 rounded"
                    style="background-color: {color(type)}"
                ></div>
                <span class="ml-2 text-white text-sm">{type} ({average.toLocaleString()})</span>
            </div>
        {/each}
    </div>
</div>

<!-- Tooltip -->
{#if tooltip.visible}
    <div
        class="absolute bg-gray-800 text-white p-2 rounded shadow"
        style="top: {tooltip.y}px; left: {tooltip.x}px"
    >
        <div class="flex items-center gap-2">
            <div
                class="w-4 h-4 rounded"
                style="background-color: {tooltip.color}"
            ></div>
            <span>{tooltip.text}</span>
        </div>
    </div>
{/if}

<style>
    .cursor-pointer {
        cursor: pointer;
    }

    .opacity-80 {
        opacity: 0.8;
    }

    .hover\:opacity-100:hover {
        opacity: 1;
    }

    .transition-opacity {
        transition: opacity 0.2s ease-in-out;
    }

    .absolute {
        position: absolute;
    }

    .bg-gray-800 {
        background-color: #2d3748;
    }

    .text-white {
        color: white;
    }

    .rounded {
        border-radius: 0.25rem;
    }

    .shadow {
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .legend {
        font-family: sans-serif;
        font-size: 14px;
    }

    .text-sm {
        font-size: 0.875rem;
    }

    .grid-cols-2 {
        grid-template-columns: repeat(2, 1fr);
    }

    .gap-4 {
        gap: 1rem;
    }

    .mt-6 {
        margin-top: 1.5rem;
    }

    .ml-2 {
        margin-left: 0.5rem;
    }
</style>
