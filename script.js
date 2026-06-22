// let arr=[20,30,40,50,60,60,303,45,6,3,3,23,34,45];
// let x=45;
// for (let ar  in arr){
//     if (x==arr[ar]){
//         console.log(ar)
//         break
//     }
// }

// function binarySearch(arr,x){
//     let left=0
//     let right=arr.length
//     let mid=Math.floor(left+right)/2
    
    
//     while(left<=right){
//         if (x==arr[mid]){
//             return mid
//         }else if(x<arr[mid]){
//             mid-=1

//         }else{
//             mid+=1
//         }
//     }
// }


// let x=binarySearch([1,2,3,4,5,6,7,8],8)
// console.log(x)



// function binary_search(arr,x,i,j){
//     let m =(i+Math.floor((j-i)/2))
//     while (i<=j){
//         if (arr[m]==x){
//             if (arr[m-1]!=x){
//                 return m
//             }
//         }else{
//             return binary_search(arguments,x,m+1,j)
//         }
//     }

// }






// let arr=[1,2,3,4,5,2,7,43,3,"x","x","x"]
// let i=0
// let j=arr.length
// let x="x"
// let res=binary_search(arr,x,i,j)
// console.log(res)




function linear_search(Arr,x){
    for (let i=0;i<=Arr.length;i++){
        if (Arr[i]==x){
            return i
        }
    }
        
    return -1;
};


let arr=[1,2,3,4,5,6,7,8,9,10]          
let x=7
let res=linear_search(arr,x)
console.log(res)    
