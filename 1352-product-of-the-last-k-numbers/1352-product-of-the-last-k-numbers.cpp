class ProductOfNumbers {
public:
    vector<int> output;

    ProductOfNumbers() {
    }
    void add(int num) {
        output.push_back(num); 
    }
    int getProduct(int k){
        long long int product=1;
        int steps=0;
        while(steps<k && steps<output.size()){
            product=product*output[output.size()-1-steps];
            steps++;
        }
        return product;
    }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */