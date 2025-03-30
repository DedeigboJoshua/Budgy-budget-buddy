// It’s a dedicated screen (not a tab) where the user can manually add a new income or expense to their account.

// Think of it like the “+” screen in your finance app — a form for logging money in or out.

import { View, Text } from 'react-native';

export default function AddTransaction() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Add Transaction Screen</Text>
    </View>
  );
}
