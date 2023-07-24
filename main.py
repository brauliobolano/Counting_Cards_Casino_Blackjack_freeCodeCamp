// Initialize the count variable to keep track of the card count.
let count = 0;

// Function to implement card counting in a card game.
function cc(card) {
  // Use a switch statement to handle different card values.
  switch (card) {
    // For cards 2 to 6 (inclusive), increment the count and print "Bet."
    case 2:
    case 3:
    case 4:
    case 5:
    case 6:
      count++;
      console.log(count + " Bet");
      break;

    // For cards 7 to 9 (inclusive), do not change the count and print "Hold."
    case 7:
    case 8:
    case 9:
      console.log(count + " Hold");
      break;

    // For cards 10, 'J', 'Q', 'K', and 'A', decrement the count and print "Hold."
    case 10:
    case 'J':
    case 'Q':
    case 'K':
    case 'A':
      count--;
      console.log(count + " Hold");
      break;
  }

  // Determine the recommendation based on the current count and return it.
  // If the count is greater than 0, suggest "Bet"; otherwise, suggest "Hold."
  return count > 0 ? count + " Bet" : count + " Hold";
}

// Example usage of the function with different cards.
cc(2); // Count: 1 Bet
cc(3); // Count: 2 Bet
cc(7); // Count: 2 Hold
cc('K'); // Count: 1 Hold
cc('A'); // Count: 0 Hold
