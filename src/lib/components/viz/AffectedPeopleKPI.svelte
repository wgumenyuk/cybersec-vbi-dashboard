<script lang="ts">
    import Card from "$components/Card.svelte";

    export let id: string;
    let affectedPeople = "Loading...";

    // Fetch or calculate `affectedPeople` based on ID
</script>

<Card class="flex flex-col items-center justify-around">
    <span class="text-silver-500">Number of Affected People</span>
    <span class="text-3xl font-bold">{affectedPeople}</span>
</Card>
